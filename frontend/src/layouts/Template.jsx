import Navigator from "../components/guest/Navigator";
import './../styles/index.css';
import './../styles/buttonStyle.css';

export default function Template({ 
    children 
}) {
    return <main className="bg-red-500 h-screen flex flex-col items-center wallpaper">
        <Navigator />

        { children }

        <footer className="w-full p-3 text-center">
            All rights reserved @ 2024
        </footer>
    </main>
}