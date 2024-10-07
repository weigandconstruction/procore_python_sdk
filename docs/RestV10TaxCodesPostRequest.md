# RestV10TaxCodesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_code** | [**RestV10TaxCodesPostRequestTaxCode**](RestV10TaxCodesPostRequestTaxCode.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_tax_codes_post_request import RestV10TaxCodesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10TaxCodesPostRequest from a JSON string
rest_v10_tax_codes_post_request_instance = RestV10TaxCodesPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10TaxCodesPostRequest.to_json())

# convert the object into a dict
rest_v10_tax_codes_post_request_dict = rest_v10_tax_codes_post_request_instance.to_dict()
# create an instance of RestV10TaxCodesPostRequest from a dict
rest_v10_tax_codes_post_request_from_dict = RestV10TaxCodesPostRequest.from_dict(rest_v10_tax_codes_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


