import {useAPI} from "../provider/APIProvider";
import {useEffect, useState} from "react";
import {useUrl} from "../provider/URLProvider";

const ScenariosPage = () => {
    const API = useAPI();
    const url = useUrl();

    const [loading, setLoading] = useState(true);
    const [scores, setScores] = useState({});

    useEffect(() => {
        const fetchScore = async () => {
            try {
                console.log(API + "api/?url=" + url);
                const response = await fetch(API + "api/?url=" + url);

                if (!response.ok) {
                    throw new Error('No data');
                }

                const result = await response.json();
                setScores(result);
            } catch (e) {
                console.log(e);
            } finally {
                setLoading(false);
            }
        }

        fetchScore();
    }, [])

    const scoreData = () => {
        return <div>
            <p>{scores.performance_score}</p>
            <p>{scores.accessibility_score}</p>
            <p>{scores.best_practices_score}</p>
        </div>
    }

    return (
        <>{loading ? <p>Loading...</p> : scoreData()}</>
    )
}

export default ScenariosPage