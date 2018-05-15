let webpack 	= require('webpack')
let path    	= require('path')

let BUILD_DIR 	= path.resolve(__dirname, 'dist')
let APP_DIR 	= path.resolve(__dirname, 'src/app')

let config = {
    entry: APP_DIR + '/index.jsx',
    output: {
        path: BUILD_DIR,
        filename: 'bundle.js',
        publicPath: '/dist/'
    },
    resolve: {
        extensions: ['.js', '.jsx', '.scss']
    },
    module: {
        loaders: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                loader: ['react-hot-loader/webpack', 'babel-loader']
            },
            {
                test: /\.scss/,
                exclude: /node_modules/,
                loader: "style-loader!css-loader!autoprefixer-loader!sass-loader"
            }
        ]
    },
    plugins: [
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: JSON.stringify(process.env.NODE_ENV)
            }
        })
    ]
}

if (process.env.NODE_ENV != 'production') {
    config.plugins.push(new webpack.NamedModulesPlugin())
    config.entry = ['react-hot-loader/patch', config.entry]
}

module.exports = config