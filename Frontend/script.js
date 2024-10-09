import { render, html } from "https://cdn.jsdelivr.net/npm/lit-html@3/+esm";

const loading = html`<div class="text-center mx-auto my-5">
  <div class="spinner-border" role="status"></div>
</div>`;

// Get form and result container elements
const $form = document.getElementById('faceSwapForm');
const $resultContainer = document.getElementById('resultContainer');
const $inputFields = document.getElementById('input-fields');

// Function to render input fields based on selected operation
function renderInputFields(operation) {
  if (operation === "enhance") {
    render(html`
      <div class="mb-3">
        <label for="sourceImage" class="form-label">Image</label>
        <input class="form-control" type="file" id="sourceImage" accept="image/*" required>
      </div>
      <div class="text-center">
        <button type="submit" class="btn btn-primary">Enhance</button>
      </div>
    `, $inputFields);
  } else {
    render(html`
      <div class="mb-3">
        <label for="sourceImage" class="form-label">Source Image (face to swap)</label>
        <input class="form-control" type="file" id="sourceImage" accept="image/*" required>
      </div>
      <div class="mb-3">
        <label for="targetImage" class="form-label">Target Image (image to put the face on)</label>
        <input class="form-control" type="file" id="targetImage" accept="image/*" required>
      </div>
      <div class="text-center">
        <button type="submit" class="btn btn-primary">Swap ${operation === "swapEnhance" ? "& Enhance" : ""}</button>
      </div>
    `, $inputFields);
  }
}

// Add event listeners to radio buttons
document.querySelectorAll('input[name="operation"]').forEach(radio => {
  radio.addEventListener('change', (e) => {
    renderInputFields(e.target.value);
  });
});

// Initial render of input fields
renderInputFields(document.querySelector('input[name="operation"]:checked').value);

$form.addEventListener('submit', async (e) => {
  e.preventDefault();

  // Get the selected operation
  const selectedOperation = document.querySelector('input[name="operation"]:checked').value;

  // Get the uploaded files
  const sourceImage = document.getElementById('sourceImage').files[0];
  const targetImage = selectedOperation !== "enhance" ? document.getElementById('targetImage').files[0] : null;

  // Create FormData object
  const formData = new FormData();

  formData.append('source', sourceImage);
  if (targetImage) formData.append('target', targetImage);
//   formData.append('operation', selectedOperation);

  // Show loading spinner
  render(loading, $resultContainer);

  try {
    // Determine which endpoint to use based on selected operation
    let endpoint = 'http://localhost:8080/';
    switch (selectedOperation) {
      case 'swap':
        endpoint += 'swap-face/';
        break;
      case 'enhance':
        endpoint += 'enhance-face/';
        break;
      case 'swapEnhance':
        endpoint += 'swap-and-enhance/';
        break;
      default:
        throw new Error('Please select an operation');
    }

    // Send POST request to backend
    const response = await fetch(endpoint, {
      method: 'POST',
      body: formData
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    } else {
      // Get the image blob from the response
      const imageBlob = await response.blob();
    
      // Create a URL for the image blob
      const imageUrl = URL.createObjectURL(imageBlob);
    
      render(
        html`
          <h3>Result</h3>
          <img id="resultImage" src="${imageUrl}" alt="Face swap result" class="img-fluid">
          <a href="${imageUrl}" download="face_swap_result.png" class="btn btn-primary mt-3">Download Result</a>
        `,
        $resultContainer
      );
    }
  } catch (error) {
    console.error('Error:', error);
    $resultContainer.innerHTML = `<p class="text-danger">Error: ${error.message}</p>`;
  }
});

