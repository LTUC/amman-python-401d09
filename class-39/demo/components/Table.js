// Destructioning

export default function Table({ answeredQuestions }) {
    //props =  {answeredQuestions : answeredQuestions}
    // props = {answeredQuestions}

    return (
        <>
            {
                answeredQuestions.length >= 1 &&
                <table className="w-1/2 mx-auto my-4">
                    <thead>
                        <tr>
                            <th className="border border-gray-600"> No.</th>
                            <th className="border border-gray-600">Question</th>
                            <th className="border border-gray-600"> Response</th>
                        </tr>
                    </thead>
                    <tbody>


                        {
                            answeredQuestions.map(item => {
                                return (
                                    <tr>
                                        <td className="border border-gray-600">{item.number}</td>
                                        <td className="border border-gray-600">{item.question}</td>
                                        <td className="border border-gray-600">{item.answer}</td>
                                    </tr>
                                )
                            })
                        }

                    </tbody>
                </table>
            }

        </>
    )
}
