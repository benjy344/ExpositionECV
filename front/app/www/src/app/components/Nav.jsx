import React 	        from 'react'
import { Link } 	    from 'react-router-dom'


class Nav extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      menuOpen: false,
      place: 1
    }
  }

  onToggle() {
    this.setState({
      menuOpen: !this.state.menuOpen
    })
  }

  togglePlace() {
    this.setState({
      place: this.state.place === 1 ? 2 : 1
    })
  }

  render() {
    return(
      <header>
        <button className={"hamburger"+(this.state.menuOpen?' is-active':'')} type="button" aria-label="Menu" aria-controls="navigation" onClick={this.onToggle.bind(this)}>
                  <span className="hamburger-box">
                    <span className="hamburger-inner"></span>
                  </span>
        </button>
        <nav className={(this.state.menuOpen?'open':'')}>
          <div className="menu-slider__content">
            <ul className="menu-items">
              <li className='item-1'>
                <Link to={`/${this.state.place === 1 ? 2 : 1 }/home`} onClick={this.togglePlace.bind(this)}>{this.state.place === 1 ? 'La Folie Numerique' : 'La Villette'}</Link>
              </li>
              <li className='item-1'>
                <Link to={`/${this.state.place}/home`}>Accueil</Link>
              </li>
              <li className='item-2'>
                <Link to="/favorites">Mes coups de coeur</Link>
              </li>
              <li className='item-3'>
                <Link to={`/${this.state.place}/infos`}>Infos Pratiques</Link>
              </li>

            </ul>
          </div>
          <div className="overlay" onClick={this.onToggle.bind(this)}></div>
        </nav>

      </header>

    )
  }
}

export default Nav