console.log("Script loaded"); // Log when the script is loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log("Calculate button clicked"); // Log when the button is clicked
    document.getElementById('calculate').addEventListener('click', function() {
        const functionInput = document.getElementById('function').value;
        const lowerLimit = parseFloat(document.getElementById('lower_limit').value);
        const upperLimit = parseFloat(document.getElementById('upper_limit').value);

        fetch('/integrate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                function: functionInput,
                lower_limit: lowerLimit,
                upper_limit: upperLimit
            })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerText = 'Result: ' + data.result;
        })
        .catch(error => {
            document.getElementById('result').innerText = 'Error: ' + error;
        });
    });
});
