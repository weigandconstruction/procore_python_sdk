# RestV10TaxTypesPostRequestTaxType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The Description of the Tax Type | [optional] 
**name** | **str** | The Name of the Tax Type | 
**origin_data** | **str** | Additional Third-party Metadata for the Tax Type. Note: This is a free-form text field. | [optional] 
**origin_id** | **str** | The Third-party ID of the Tax Type | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_tax_types_post_request_tax_type import RestV10TaxTypesPostRequestTaxType

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10TaxTypesPostRequestTaxType from a JSON string
rest_v10_tax_types_post_request_tax_type_instance = RestV10TaxTypesPostRequestTaxType.from_json(json)
# print the JSON string representation of the object
print(RestV10TaxTypesPostRequestTaxType.to_json())

# convert the object into a dict
rest_v10_tax_types_post_request_tax_type_dict = rest_v10_tax_types_post_request_tax_type_instance.to_dict()
# create an instance of RestV10TaxTypesPostRequestTaxType from a dict
rest_v10_tax_types_post_request_tax_type_from_dict = RestV10TaxTypesPostRequestTaxType.from_dict(rest_v10_tax_types_post_request_tax_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


