import { useState, useEffect } from 'react';


function Form() {
    // states: 
    // const [state , setState] =  useState('default value');
    const [userInput, setUserInput] = useState("change"); // null
    const [submitInput, setSubmitInput] = useState("submit");

    // Causing an error
    if (userInput === 'x') {
        throw new Error("I have crashed");
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log("Form has been submitted");
        const userFormInput = e.target.userText.value;
        setSubmitInput(userFormInput);
    }

    const handleChange = (e) => {
        console.log("Input is changing");
        const userFormInput = e.target.value; // e.target.userText.value

        setUserInput(userFormInput);
    }

    console.log('Form is rendering')
    // mounted
    useEffect(() => {
        document.title = submitInput;
    }, [submitInput]);

    return (
        <>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="Enter page title" name="userText" onChange={handleChange} />
                <input type="submit" value="Submit Form" />
            </form>

            <p>on change : {userInput}</p>
            <p>on submit: {submitInput}</p>
        </>
    )
}

export default Form;