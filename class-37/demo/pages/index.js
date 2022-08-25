import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import Link from 'next/link'
import { useState } from 'react';
import { replies } from '../data.js';

export default function Home() {
  const [answeredQuestions, setAnsweredQuestions] = useState([]); // array of objects where each object represnt the question object

  function handleUserQuestion(e) {
    e.preventDefault();
    console.log("Form has been submitted");
    const randomIndex = Math.floor(Math.random() * replies.length) // from w3school

    const questionObject = {
      question: e.target.question.value,
      answer: replies[randomIndex],
      number: answeredQuestions.length + 1,
    }
    // spread operator
    // setAnsweredQuestions(questionObject);
    setAnsweredQuestions([...answeredQuestions, questionObject])

    console.log(1111111, answeredQuestions)
    console.log(2222222, questionObject)

  }

  return (
    <div className="">
      <Head>
        <title>8 Magic Ball</title>
        <meta name="description" content="ask random questions to get random replies" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <header className="flex justify-between bg-gray-400  text-gray-50 p-4">
        <h1 className=" text-2xl">
          8 Magic Ball
        </h1>
        <p>{answeredQuestions.length} questions answered</p>
      </header>

      <main className="">
        {/* Form section */}
        <form onSubmit={handleUserQuestion} className="mx-auto my-4 flex w-1/2 bg-gray-200 p-2">
          <input className="flex-auto pl-1" type="text" name="question" placeholder="Ask me Anything" />
          <input className="text-gray-50 bg-gray-600 px-2 py-1" type="submit" value="Ask" />
        </form>
        {/* ball section  */}
        <div className="bg-gray-800 w-96 h-96 rounded-full mx-auto my-4">
          <div className="bg-gray-50 flex item-center relative top-16 left-16 justify-center rounded-full 
          w-44 h-44">
            <p className="text-center mt-14 text-xl">
              {answeredQuestions?.at(-1)?.answer}
            </p>
          </div>
        </div>
        {/* table section  */}
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


      </main>
      <footer className="bg-gray-400  text-gray-50 p-4 mt-8 mb-0">
        <Link href="careers">
          <a className="text-2xl" target="_blank"> Careers </a>
        </Link>
      </footer>
    </div>
  )
}
