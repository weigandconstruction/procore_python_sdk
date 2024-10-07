# RestV10TaxTypesIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_type** | [**RestV10TaxTypesIdPatchRequestTaxType**](RestV10TaxTypesIdPatchRequestTaxType.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_tax_types_id_patch_request import RestV10TaxTypesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10TaxTypesIdPatchRequest from a JSON string
rest_v10_tax_types_id_patch_request_instance = RestV10TaxTypesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10TaxTypesIdPatchRequest.to_json())

# convert the object into a dict
rest_v10_tax_types_id_patch_request_dict = rest_v10_tax_types_id_patch_request_instance.to_dict()
# create an instance of RestV10TaxTypesIdPatchRequest from a dict
rest_v10_tax_types_id_patch_request_from_dict = RestV10TaxTypesIdPatchRequest.from_dict(rest_v10_tax_types_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


