import MagicBallHome from '../components/MagicBallHome';
import { AuthContext } from '../contexts/Auth'; // 1. importing the context that has your global state
import { useContext } from 'react'; // 2
import LoginForm from '../components/LoginForm'

// if I have a token, render MagicBallHome else Login form

export default function Home() {
  const { tokens } = useContext(AuthContext); // 3
  console.log("global state coming form Context", tokens)

  return (
    <>
      {
        (tokens) ? <MagicBallHome /> : <LoginForm />
      }

    </>
  )
}