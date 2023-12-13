import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Navigation } from "./components/Navigation";
import { HomePage } from "./pages/HomePage"
import { LoginPage } from "./pages/LoginPage";
import { ContactPage } from "./pages/ContactPage";
import { HelpPage } from "./pages/HelpPage";

function App() {

  return (
    <BrowserRouter>
      <Navigation />
      <Routes>
        <Route path="/" element={<HomePage />}></Route>
        <Route path="/login" element={<LoginPage />}></Route>
        <Route path="/contacto" element={<ContactPage />}></Route>
        <Route path="/ayuda" element={<HelpPage />}></Route>
      </Routes>
    </BrowserRouter>
  )
}


export default App