export { Get }

const BaseUrl = 'https://drive-test-conqueror.herokuapp.com/api/'

async function Get(url) {
  try {
    const response = await fetch(`${BaseUrl}${url}/`);
    console.log("GET", url, response.status)
    const responseText = await response.text()
    const responseJson = responseText.length ? JSON.parse(responseText) : null
    return { status: response.status, data: responseJson };
  } catch (error) {
    throw new Error(`Fetch Error:\n${error}`)
  }
}