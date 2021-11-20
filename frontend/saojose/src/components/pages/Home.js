import styles from './Home.module.css';
import { useEffect, useState } from 'react';
import ListSpecialty from '../layouts/ListSpecialty';


function Home() {
    const URL = 'http://localhost:3001/';
    const [especialidades, setEspecialidades] = useState([]);

    useEffect(() => {
        fetch(URL, {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            } 
        })
            .then((resp) => resp.json())
            .then((data) => {
                console.log(data)
                setEspecialidades(data);
            })
            .catch((err) => console.log(err))
    }, [])

    return (
        <div className={styles.container}>
            
            <div className={styles.title_container}>
                <h1>Especialidades</h1>
            </div>

            <div className={styles.speciality_container}>
                {especialidades.length > 0 && (
                        especialidades.map(especialidade => (
                            <ListSpecialty specialty_name={especialidade.name} specialty_link={especialidade.link}></ListSpecialty>
                        ))
                    )
                }
            </div>
        </div>
        
    );
}

export default Home;