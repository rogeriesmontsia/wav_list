import '../App.css'
import { Outlet, Route, Routes } from 'react-router-dom'
export default function Home() {
    return (
        <div >
          
            <main className="h-96 flex-1 bg-blue-50 p-4">
                <Outlet />
            </main>

            
        </div>

    )
}


