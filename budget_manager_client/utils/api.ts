import axios from 'axios';

export const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000/api',
});

export const axiosGET = (url: string, setData: React.SetStateAction<any>) => {
  axiosInstance
    .get(url)
    .then(response => {
      setData(response.data);
    })
    .catch(error => {
      console.log(error);
      alert(error.request.response);
    });
};

export const axiosPOST = (url: string, data: any, setData: React.SetStateAction<any>) => {
  axiosInstance
    .post(url, data)
    .then(respone => {
      console.log(respone.data);
      setData;
    })
    .catch(error => {
      console.log(error.request.response);
      alert(error.request.response);
    });
};
