import Link from 'next/link'

export default function Footer() {
    return (
        <footer className="p-4 mt-8 mb-0 bg-gray-400 text-gray-50">
            <Link href="careers">
                <a className="text-2xl" target="_blank"> Careers </a>
            </Link>
        </footer>
    )
}