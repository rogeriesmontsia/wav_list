import './App.css'
import { Route, Routes } from 'react-router-dom'
import { DashboardLayout, LoginLayout } from './layout'
import { Home } from './pages'
import { Login } from './pages'
import { List } from './pages'
import { NotFound } from './pages'
import { Discover } from './pages'
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
                <Route path="api" element={<Discover />} />
              </Routes>
            </DashboardLayout>
          }
        />
        <Route path='*' element={<NotFound />}/>
      </Routes>
    </>
  )
}

export default App
