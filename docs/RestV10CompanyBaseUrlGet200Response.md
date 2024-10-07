# RestV10CompanyBaseUrlGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone** | **str** | zone request will be routed to | [optional] 
**web_base_url** | **str** | base_url for routed zone | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_company_base_url_get200_response import RestV10CompanyBaseUrlGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompanyBaseUrlGet200Response from a JSON string
rest_v10_company_base_url_get200_response_instance = RestV10CompanyBaseUrlGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CompanyBaseUrlGet200Response.to_json())

# convert the object into a dict
rest_v10_company_base_url_get200_response_dict = rest_v10_company_base_url_get200_response_instance.to_dict()
# create an instance of RestV10CompanyBaseUrlGet200Response from a dict
rest_v10_company_base_url_get200_response_from_dict = RestV10CompanyBaseUrlGet200Response.from_dict(rest_v10_company_base_url_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


