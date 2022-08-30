
export default function Form(props) {
    console.log(props)

    function handleSubmit(e) {
        e.preventDefault();
        // e.target.question.value
        // calling the function (the one send form the parent)
        
        props.getUserInput(e.target.question.value)
    }

    return (
        <form onSubmit={handleSubmit} className="flex w-1/2 p-2 mx-auto my-4 bg-gray-200">
            <input className="flex-auto pl-1" type="text" name="question" placeholder="Ask me Anything" required />
            <input className="px-2 py-1 bg-gray-600 text-gray-50" type="submit" value="Ask" />
        </form>
    )
}