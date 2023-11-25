import WebsiteForm from "./WebsiteForm";
import logo from "../assets/images/LOGO.svg"

const EnteryPage = () => {
    return (
        <>
            <img src={logo} alt={"UXplorer"}/>
            <div className={"WebsiteForm-background"}>
                <WebsiteForm/>
            </div>
        </>
    )
}

export default EnteryPage;