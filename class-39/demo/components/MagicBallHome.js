import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import { useState } from 'react';
import { replies } from '../data.js';
import useSWR from 'swr'
import axios from 'axios';
import { AuthContext } from '../contexts/Auth';
import { useContext } from 'react';


// import components from one place(components/index)
import { Header, Footer, Ball, Form, Table } from '../components';
const url = 'https://api-8-magic-balls.herokuapp.com/api/v1/answers/'

export default function MagicBallHome() {
    const { tokens } = useContext(AuthContext)
    const [answeredQuestions, setAnsweredQuestions] = useState([]); // array of objects where each object represnt the question object

    const config = {
        headers: {
            'Authorization': `Bearer ${tokens.access}`
        }
    }

    console.log(config)
    const fetcher = url => axios.get(url, config).then(res => res.data)
    const { data, error } = useSWR(url, fetcher)


    function getUserInput(userInput) {
        // userInput value is going to come from the child
        // filter array method, I use it to loop through an array and filter values based on a condition. returns an array of the elements that match the condition

        let isExistArr = answeredQuestions.filter((item) => item.question === userInput)

        if (isExistArr.length === 1) {
            alert("No second try! one answer only");
            return;
        }

        const randomIndex = Math.floor(Math.random() * replies.length);
        const questionObject = {
            question: userInput,
            answer: replies[randomIndex],
            number: answeredQuestions.length + 1,
        }
        setAnsweredQuestions([...answeredQuestions, questionObject])
    }

    if (tokens && !data) return <div>loading...</div>
    console.log({ data });
    return (
        <div className="">
            <Head>
                <title>8 Magic Ball</title>
                <meta name="description" content="ask random questions to get random replies" />
                <link rel="icon" href="/favicon.ico" />
            </Head>

            <Header count={answeredQuestions.length} />

            <main className="">
                {/* Form section */}
                <Form getUserInput={getUserInput} />
                {/* ball section  */}
                <Ball answeredQuestions={answeredQuestions} />
                {/* table section  */}
                <Table answeredQuestions={answeredQuestions} />
            </main>
            <Footer />
        </div>
    )
}
