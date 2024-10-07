# CompanyVendorBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | 
**vendor** | [**CompanyVendor**](CompanyVendor.md) |  | 

## Example

```python
from procore_sdk.models.company_vendor_body import CompanyVendorBody

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyVendorBody from a JSON string
company_vendor_body_instance = CompanyVendorBody.from_json(json)
# print the JSON string representation of the object
print(CompanyVendorBody.to_json())

# convert the object into a dict
company_vendor_body_dict = company_vendor_body_instance.to_dict()
# create an instance of CompanyVendorBody from a dict
company_vendor_body_from_dict = CompanyVendorBody.from_dict(company_vendor_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


