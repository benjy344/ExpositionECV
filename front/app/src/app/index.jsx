import React 	        from 'react'
import ReactDom         from 'react-dom'
import { Provider }     from 'react-redux'
import { AppContainer } from 'react-hot-loader'

import Store            from './generalStore/Store'
import App 		        from './components/App'


const renderApp = () => {
    ReactDom.render(
        <AppContainer>
            <Provider store={Store}>
                <App />
            </Provider>
        </AppContainer>,
        document.getElementById('app')
    )
}

if (module.hot) {
    module.hot.accept('./components/App', renderApp)
}

renderApp()

if (module.hot) {
  	module.hot.accept('./components/App', renderApp)
}

renderApp()