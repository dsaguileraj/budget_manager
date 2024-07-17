import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000/api',
});

export const axiosGET = (url: string, data: object, setData: () => void) => {
  axiosInstance
    .get(url, data)
    .then(respone => {
      console.log(respone.data);
      setData;
    })
    .catch(error => {
      console.log(error);
      alert('Se ha producido un error');
    });
};
export const axiosPATCH = (url: string, data: object, setData: () => void) => {
  axiosInstance
    .patch(url, data)
    .then(respone => {
      console.log(respone.data);
      setData;
    })
    .catch(error => {
      console.log(error);
      alert('Se ha producido un error');
    });
};

export const axiosPOST = (url: string, data: object, setData: () => void) => {
  axiosInstance
    .post(url, data)
    .then(respone => {
      console.log(respone.data);
      setData;
    })
    .catch(error => {
      console.log(error);
      alert('Se ha producido un error');
    });
};
