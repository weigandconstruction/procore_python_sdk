# RestV10TaxCodesIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_code** | [**RestV10TaxCodesIdPatchRequestTaxCode**](RestV10TaxCodesIdPatchRequestTaxCode.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_tax_codes_id_patch_request import RestV10TaxCodesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10TaxCodesIdPatchRequest from a JSON string
rest_v10_tax_codes_id_patch_request_instance = RestV10TaxCodesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10TaxCodesIdPatchRequest.to_json())

# convert the object into a dict
rest_v10_tax_codes_id_patch_request_dict = rest_v10_tax_codes_id_patch_request_instance.to_dict()
# create an instance of RestV10TaxCodesIdPatchRequest from a dict
rest_v10_tax_codes_id_patch_request_from_dict = RestV10TaxCodesIdPatchRequest.from_dict(rest_v10_tax_codes_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


