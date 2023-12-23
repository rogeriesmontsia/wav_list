import '../App.css'
import { Outlet, Route, Routes } from 'react-router-dom'
import { Discover } from '../pages'
export default function Home() {
    return (
        <div >
          
            <main className="h-96 flex-1 bg-blue-50 p-4">
                <Outlet />
            </main>

            <footer className="bg-blue-200 p-4">Footer</footer>
        </div>

    )
}


