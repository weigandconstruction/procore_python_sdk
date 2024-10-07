# RestV10CompanyBaseUrlGet400ResponseError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | error code | [optional] 
**message** | **str** | error message | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_company_base_url_get400_response_error import RestV10CompanyBaseUrlGet400ResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompanyBaseUrlGet400ResponseError from a JSON string
rest_v10_company_base_url_get400_response_error_instance = RestV10CompanyBaseUrlGet400ResponseError.from_json(json)
# print the JSON string representation of the object
print(RestV10CompanyBaseUrlGet400ResponseError.to_json())

# convert the object into a dict
rest_v10_company_base_url_get400_response_error_dict = rest_v10_company_base_url_get400_response_error_instance.to_dict()
# create an instance of RestV10CompanyBaseUrlGet400ResponseError from a dict
rest_v10_company_base_url_get400_response_error_from_dict = RestV10CompanyBaseUrlGet400ResponseError.from_dict(rest_v10_company_base_url_get400_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


