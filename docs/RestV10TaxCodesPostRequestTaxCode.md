# RestV10TaxCodesPostRequestTaxCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The Tax Code | 
**description** | **str** | The Description of the Tax Code | [optional] 
**origin_data** | **str** | Additional Third-party Metadata for the Tax Code. Note: This is a free-form text field. | [optional] 
**origin_id** | **str** | The Third-party ID of the Tax Code | [optional] 
**rate1** | **float** | Rate to apply for first Tax Type | [optional] 
**archived** | **bool** | Set to true if this tax code has been archived | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_tax_codes_post_request_tax_code import RestV10TaxCodesPostRequestTaxCode

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10TaxCodesPostRequestTaxCode from a JSON string
rest_v10_tax_codes_post_request_tax_code_instance = RestV10TaxCodesPostRequestTaxCode.from_json(json)
# print the JSON string representation of the object
print(RestV10TaxCodesPostRequestTaxCode.to_json())

# convert the object into a dict
rest_v10_tax_codes_post_request_tax_code_dict = rest_v10_tax_codes_post_request_tax_code_instance.to_dict()
# create an instance of RestV10TaxCodesPostRequestTaxCode from a dict
rest_v10_tax_codes_post_request_tax_code_from_dict = RestV10TaxCodesPostRequestTaxCode.from_dict(rest_v10_tax_codes_post_request_tax_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


