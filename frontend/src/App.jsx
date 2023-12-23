import './App.css'
import { Route, Routes } from 'react-router-dom'
import { DashboardLayout, LoginLayout } from './layout'
import { Home } from './pages'
import { Login } from './pages'
import { List } from './pages'
function App() {

  return (
    <>
      <Routes>
        <Route path="/login" element={<LoginLayout><Login /></LoginLayout>} />
        <Route
          path="/dashboard/*"
          element={
            <DashboardLayout>
              <Routes>
                <Route index element={<Home />} />
                <Route path="test" element={<List />} />
              </Routes>
            </DashboardLayout>
          }
        />
      </Routes>
    </>
  )
}

export default App
