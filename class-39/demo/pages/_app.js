import '../styles/globals.css';
import { AuthWrapper } from '../contexts/Auth';

function MyApp({ Component, pageProps }) {
  return (
    <>
      <AuthWrapper>
        <Component {...pageProps} />
      </AuthWrapper>
    </>
  )
}

export default MyApp