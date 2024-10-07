# procore_sdk.AuthenticationOAuth20AuthenticationApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_authorize_get**](AuthenticationOAuth20AuthenticationApi.md#oauth_authorize_get) | **GET** /oauth/authorize | Grant App Authorization
[**oauth_revoke_post**](AuthenticationOAuth20AuthenticationApi.md#oauth_revoke_post) | **POST** /oauth/revoke | Revoke Token
[**oauth_token_info_get**](AuthenticationOAuth20AuthenticationApi.md#oauth_token_info_get) | **GET** /oauth/token/info | Get Token Info
[**oauth_token_post**](AuthenticationOAuth20AuthenticationApi.md#oauth_token_post) | **POST** /oauth/token | Get or Refresh an Access Token


# **oauth_authorize_get**
> RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response oauth_authorize_get(response_type, client_id, redirect_uri)

Grant App Authorization

Creates and returns a temporary authorization code with 10 minute expiration. Note that all parameters listed below are required. This endpoint corresponds to the OAuth 2.0 authorization endpoint described in section 3.1 of the OAuth 2.0 RFC. See the [Authentication Guide](/documentation/oauth-introduction) for additional information and authentication examples.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_companies_company_id_workflow_permanent_logs_get401_response import RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response
from procore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.procore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = procore_sdk.Configuration(
    host = "https://api.procore.com"
)


# Enter a context with an instance of the API client
with procore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = procore_sdk.AuthenticationOAuth20AuthenticationApi(api_client)
    response_type = 'code' # str | Response type. Value should be `code` for server apps, `token` for client apps.
    client_id = '76ba4c5c75c96f6087f58a4de10be6c00b29ea1ddc3b2022ee2016d1363e3a7c' # str | Client ID you were assigned when you registered your application.
    redirect_uri = 'http://localhost' # str | The URI that the user will be redirected to after they grant authorization to your application. For browser-based web applications, use a `https://` web address. For \"headless\" applications use `urn:ietf:wg:oauth:2.0:oob`.

    try:
        # Grant App Authorization
        api_response = api_instance.oauth_authorize_get(response_type, client_id, redirect_uri)
        print("The response of AuthenticationOAuth20AuthenticationApi->oauth_authorize_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationOAuth20AuthenticationApi->oauth_authorize_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_type** | **str**| Response type. Value should be &#x60;code&#x60; for server apps, &#x60;token&#x60; for client apps. | 
 **client_id** | **str**| Client ID you were assigned when you registered your application. | 
 **redirect_uri** | **str**| The URI that the user will be redirected to after they grant authorization to your application. For browser-based web applications, use a &#x60;https://&#x60; web address. For \&quot;headless\&quot; applications use &#x60;urn:ietf:wg:oauth:2.0:oob&#x60;. | 

### Return type

[**RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet401Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to the specified &#x60;redirect_uri&#x60; |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_revoke_post**
> object oauth_revoke_post(procore_company_id, oauth_revoke_post_request)

Revoke Token

Revoke authorization of an access token. The request must contain the body data as form-data. The authorization server responds with HTTP status code 200 if the token has been revoked successfully or if the client submitted an invalid token. Note that the Revoke Token endpoint revokes both the Access Token and Refresh Token. The `client_secret` param is only required for confidential applications. Public applications using the implicit OAuth flow do not need to provide this parameter to revoke access tokens.

### Example


```python
import procore_sdk
from procore_sdk.models.oauth_revoke_post_request import OauthRevokePostRequest
from procore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.procore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = procore_sdk.Configuration(
    host = "https://api.procore.com"
)


# Enter a context with an instance of the API client
with procore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = procore_sdk.AuthenticationOAuth20AuthenticationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    oauth_revoke_post_request = procore_sdk.OauthRevokePostRequest() # OauthRevokePostRequest | 

    try:
        # Revoke Token
        api_response = api_instance.oauth_revoke_post(procore_company_id, oauth_revoke_post_request)
        print("The response of AuthenticationOAuth20AuthenticationApi->oauth_revoke_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationOAuth20AuthenticationApi->oauth_revoke_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **oauth_revoke_post_request** | [**OauthRevokePostRequest**](OauthRevokePostRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_token_info_get**
> OauthTokenInfoGet200Response oauth_token_info_get()

Get Token Info

Return access token details. See the [Authentication Guide](/documentation/oauth-introduction) for additional information and authentication examples. The request must contain the access token in the Authorization header: `Authorization: Bearer <YOUR_ACCESS_TOKEN>`

### Example


```python
import procore_sdk
from procore_sdk.models.oauth_token_info_get200_response import OauthTokenInfoGet200Response
from procore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.procore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = procore_sdk.Configuration(
    host = "https://api.procore.com"
)


# Enter a context with an instance of the API client
with procore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = procore_sdk.AuthenticationOAuth20AuthenticationApi(api_client)

    try:
        # Get Token Info
        api_response = api_instance.oauth_token_info_get()
        print("The response of AuthenticationOAuth20AuthenticationApi->oauth_token_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationOAuth20AuthenticationApi->oauth_token_info_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OauthTokenInfoGet200Response**](OauthTokenInfoGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_token_post**
> OauthTokenPost200Response oauth_token_post(oauth_token_post_request)

Get or Refresh an Access Token

Used to acquire a new access token or refresh an existing access token. Certain parameter combinations and values are used depending on which scenario you are handling. See the individual parameter descriptions for additional information. This endpoint corresponds to the token endpoint described in section 3.2 of the OAuth 2.0 RFC. See the [Authentication Guide](/documentation/oauth-introduction) for additional information and authentication examples. JavaScript applications cannot make this request to get the access token or refresh token.

### Example


```python
import procore_sdk
from procore_sdk.models.oauth_token_post200_response import OauthTokenPost200Response
from procore_sdk.models.oauth_token_post_request import OauthTokenPostRequest
from procore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.procore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = procore_sdk.Configuration(
    host = "https://api.procore.com"
)


# Enter a context with an instance of the API client
with procore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = procore_sdk.AuthenticationOAuth20AuthenticationApi(api_client)
    oauth_token_post_request = procore_sdk.OauthTokenPostRequest() # OauthTokenPostRequest | 

    try:
        # Get or Refresh an Access Token
        api_response = api_instance.oauth_token_post(oauth_token_post_request)
        print("The response of AuthenticationOAuth20AuthenticationApi->oauth_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationOAuth20AuthenticationApi->oauth_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_token_post_request** | [**OauthTokenPostRequest**](OauthTokenPostRequest.md)|  | 

### Return type

[**OauthTokenPost200Response**](OauthTokenPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

