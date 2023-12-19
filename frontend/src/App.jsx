import { BrowserRouter, Routes, Route } from "react-router-dom"; 
import { Home } from "./pages/shared/Home"
import { LoginPage } from "./pages/guest/auth/Login";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />}></Route>
                <Route path="/login" element={<LoginPage />}></Route>
            </Routes>
        </BrowserRouter>
    ) 
}

export default App