# RestV10TaxTypesSyncPatch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[RestV10TaxTypesGet200ResponseInner]**](RestV10TaxTypesGet200ResponseInner.md) |  | [optional] 
**errors** | [**List[RestV10TaxTypesSyncPatch200ResponseErrorsInner]**](RestV10TaxTypesSyncPatch200ResponseErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_tax_types_sync_patch200_response import RestV10TaxTypesSyncPatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10TaxTypesSyncPatch200Response from a JSON string
rest_v10_tax_types_sync_patch200_response_instance = RestV10TaxTypesSyncPatch200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10TaxTypesSyncPatch200Response.to_json())

# convert the object into a dict
rest_v10_tax_types_sync_patch200_response_dict = rest_v10_tax_types_sync_patch200_response_instance.to_dict()
# create an instance of RestV10TaxTypesSyncPatch200Response from a dict
rest_v10_tax_types_sync_patch200_response_from_dict = RestV10TaxTypesSyncPatch200Response.from_dict(rest_v10_tax_types_sync_patch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


