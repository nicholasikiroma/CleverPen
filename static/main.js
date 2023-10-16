async function callOpenAI(text) {
    const response = await fetch('/openai', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    });
    const json = await response.json();
    return json;
}


const inputForm = document.getElementById('input-form');
const inputText = document.getElementById('input-text');
const responseForm = document.getElementById('response-form');
const responseText = document.getElementById('response-text');
//let editor;

inputForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const response = await callOpenAI(inputText.value);
    CKEDITOR.instances['response-text'].setData(response.response_text)
    //    responseText.innerHTML = response.response_text;

});