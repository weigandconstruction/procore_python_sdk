# RestV10TaxCodesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the Tax Code | [optional] 
**code** | **str** | The Tax Code | [optional] 
**description** | **str** | Description of the Tax Code | [optional] 
**origin_data** | **str** | Additional Third-party Metadata for the Tax Code. Note: This is a free-form text field. | [optional] 
**origin_id** | **str** | The Third-party ID of the Tax Code | [optional] 
**rate1** | **float** | Rate to apply for first Tax Type | [optional] 
**archived** | **bool** | Set to true if this tax code has been archived | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_tax_codes_get200_response_inner import RestV10TaxCodesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10TaxCodesGet200ResponseInner from a JSON string
rest_v10_tax_codes_get200_response_inner_instance = RestV10TaxCodesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10TaxCodesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_tax_codes_get200_response_inner_dict = rest_v10_tax_codes_get200_response_inner_instance.to_dict()
# create an instance of RestV10TaxCodesGet200ResponseInner from a dict
rest_v10_tax_codes_get200_response_inner_from_dict = RestV10TaxCodesGet200ResponseInner.from_dict(rest_v10_tax_codes_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


