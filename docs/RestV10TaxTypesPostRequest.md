# RestV10TaxTypesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_type** | [**RestV10TaxTypesPostRequestTaxType**](RestV10TaxTypesPostRequestTaxType.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_tax_types_post_request import RestV10TaxTypesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10TaxTypesPostRequest from a JSON string
rest_v10_tax_types_post_request_instance = RestV10TaxTypesPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10TaxTypesPostRequest.to_json())

# convert the object into a dict
rest_v10_tax_types_post_request_dict = rest_v10_tax_types_post_request_instance.to_dict()
# create an instance of RestV10TaxTypesPostRequest from a dict
rest_v10_tax_types_post_request_from_dict = RestV10TaxTypesPostRequest.from_dict(rest_v10_tax_types_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


