import { Link } from 'react-router-dom';
import Container from './Container';
import styles from './Navbar.module.css';


function Navbar() {
    return (
        <nav className={styles.navbar}>
            <Container>
                <Link to="/" style={{ textDecoration: 'none' }} className={styles.title_navbar}>Clínica São José</Link>
            </Container>
      </nav>
    )
}

export default Navbar;