import React, {useState} from 'react';
import logo from "../assets/images/LOGO.svg";
import vector1 from "../assets/images/Background_svg/Vector 1.svg";
import vector2 from "../assets/images/Background_svg/Vector 2.svg";
import vector3 from "../assets/images/Background_svg/Vector 3.svg";
import vector4 from "../assets/images/Background_svg/Vector 4.svg";
import vector6 from "../assets/images/Background_svg/Vector 6.svg";
import vector7 from "../assets/images/Background_svg/Vector 7.svg";

const Background = ({children}) => {
    const [isHovered, setIsHovered] = useState(false);

    const handleMouseEnter = () => {
        setIsHovered(true);
    };

    const handleMouseLeave = () => {
        setIsHovered(false);
    };

    return (
        <>
            <div className={"block-bg"}>
                <div onMouseEnter={handleMouseEnter}
                    onMouseLeave={handleMouseLeave}>
                    {children}
                </div>
            </div>
            <div className="Background">
                <div className="svg-vertical-group">
                    <img src={logo} alt="UXplorer" className="logo"/>
                    <img style={{filter: isHovered ? 'none' : 'blur(3px)'}}
                         src={vector1} alt="" className="bg-vector-1"/>
                    <img style={{filter: isHovered ? 'none' : 'blur(3px)'}}
                         src={vector2} alt="" className="bg-vector-2"/>
                    <img style={{filter: isHovered ? 'none' : 'blur(3px)'}}
                         src={vector3} alt="" className="bg-vector-3"/>
                </div>
                <div className="svg-vertical-group">
                    <img style={{filter: isHovered ? 'none' : 'blur(3px)'}}
                         src={vector4} alt="" className="bg-vector-4"/>
                </div>
                <div className="svg-vertical-group">
                    <img style={{filter: isHovered ? 'none' : 'blur(3px)'}}
                         src={vector6} alt="" className="bg-vector-6"/>
                    <img style={{filter: isHovered ? 'none' : 'blur(3px)'}}
                         src={vector7} alt="" className="bg-vector-7"/>
                </div>
            </div>
        </>
    )
};

export default Background;