import logo from "../assets/images/LOGO.svg"
import vector1 from "../assets/images/Background_svg/Vector 1.svg"
import vector2 from "../assets/images/Background_svg/Vector 2.svg"
import vector3 from "../assets/images/Background_svg/Vector 3.svg"
import vector4 from "../assets/images/Background_svg/Vector 4.svg"
import vector6 from "../assets/images/Background_svg/Vector 6.svg"
import vector7 from "../assets/images/Background_svg/Vector 7.svg"


const Background = ({children}) => {
    return (
        <>
            {children}
            <div className={"Background"}>
                <div className={"svg-vertical-group"}>
                    <img src={logo} alt={"UXplorer"} className={"logo"}/>
                    <img src={vector1} alt={""} className={"bg-vector-1"}/>
                    <img src={vector2} alt={""} className={"bg-vector-2"}/>
                    <img src={vector3} alt={""} className={"bg-vector-3"}/>
                </div>
                <div className={"svg-vertical-group"}>
                    <img src={vector4} alt={""} className={"bg-vector-4"}/>
                </div>
                <div className={"svg-vertical-group"}>
                    <img src={vector6} alt={""} className={"bg-vector-6"}/>
                    <img src={vector7} alt={""} className={"bg-vector-7"}/>
                </div>
            </div>
        </>
    )
}

export default Background;