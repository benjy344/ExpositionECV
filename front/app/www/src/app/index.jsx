import React 	        from 'react'
import ReactDom         from 'react-dom'
import { Provider }     from 'react-redux'
import { AppContainer } from 'react-hot-loader'
import { ConnectedRouter } from 'react-router-redux'
import { Route }         from 'react-router'

import { Store, history} from './generalStore/Store'
import App 		         from './components/App'
import Nav 		         from './components/Nav'
import About 		     from './components/About'

import './scss/main.scss'
import Artwork from "./components/Artwork";

const renderApp = () => {
    ReactDom.render(
        <AppContainer>
            <Provider store={Store}>
                <div>
                    <ConnectedRouter history={history}>
                        <div>
                            <Nav />
                            <Route exact path="/" component={App}/>
                            <Route path="/about" component={About}/>
                            <Route path="/artwork/:id" component={Artwork}/>
                        </div>
                    </ConnectedRouter>
                </div>
            </Provider>
        </AppContainer>,
        document.getElementById('app')
    )
}


if (module.hot) {
  	module.hot.accept('./components/App', renderApp)
}

renderApp()