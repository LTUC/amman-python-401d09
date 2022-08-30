export default function Header(props) {
    // funtion that will update the count
    return (
        <header className="flex justify-between p-4 bg-gray-400 text-gray-50">
            <h1 className="text-2xl ">
                8 Magic Ball
            </h1>
            {/* <p>{props.count} questions answered</p> */}
            <p>
                {props.count}  {props.count > 1 ? "questions answered" : "question answered"}
            </p>
        </header>
    )
}