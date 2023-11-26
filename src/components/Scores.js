import performance from "../assets/images/performance_score.svg"
import accessibility from "../assets/images/accessibility_score.svg"
import best_practice from "../assets/images/best_practice_score.svg"
import divider from "../assets/images/divider.svg"


const Scores = () => {
    return (
        <div className={"Scores"}>
            <img src={divider} alt={""} className={"divider"}/>
            <div className={"Scores-objects"}>
                <div>
                    <img src={performance} alt={""}/>
                    <p>Performance</p>
                </div>
                <div>
                    <img src={accessibility} alt={""}/>
                    <p>Accessibility</p>
                </div>
                    <div>
                        <img src={best_practice} alt={""}/>
                        <p>Best Practice</p>
                    </div>
            </div>
        </div>
    )
}

export default Scores