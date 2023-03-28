import axios from 'axios'

let $axios = axios.create({
  baseURL: '/api/',
  timeout: 5000,
  headers: {'Content-Type': 'application/json'}
})

const location = { protocol: 'http:', hostname: '127.0.0.1', port: '8000' }
$axios.defaults.baseURL = location.protocol + '//' + location.hostname + ':' + location.port;

// Request Interceptor
$axios.interceptors.request.use(function (config) {
  config.headers['Authorization'] = 'Fake Token'
  return config
})

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // Handle Error
  console.log(error)
  return Promise.reject(error)
})

export default {
  createAuthor(data) {
    return $axios.post('api/author/', data);
  },
  fetchAuthors() {
    return $axios.get('api/author/');
  },
  createNote(data) {
    return $axios.post('api/note/', data);
  },
  fetchNotes() {
    return $axios.get('api/note/');
  },
}
