export default function Ball(props) {
    return (
        <div className="mx-auto my-4 bg-gray-800 rounded-full w-96 h-96">
            <div className="relative flex justify-center rounded-full bg-gray-50 item-center top-16 left-16 w-44 h-44">
                <p className="text-xl text-center mt-14">
                    {/* optional chaining */}
                    {/* {props.answeredQuestions.at(-1)?.answer} */}
                    {
                        props.answeredQuestions.at(-1) ?
                            props.answeredQuestions.at(-1).answer :
                            "Ask and I shall answer"
                    }
                </p>
            </div>
        </div>
    )
}