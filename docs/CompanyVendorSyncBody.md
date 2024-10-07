# CompanyVendorSyncBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | 
**updates** | [**List[CompanyVendorSyncBodyUpdatesInner]**](CompanyVendorSyncBodyUpdatesInner.md) |  | 

## Example

```python
from procore_sdk.models.company_vendor_sync_body import CompanyVendorSyncBody

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyVendorSyncBody from a JSON string
company_vendor_sync_body_instance = CompanyVendorSyncBody.from_json(json)
# print the JSON string representation of the object
print(CompanyVendorSyncBody.to_json())

# convert the object into a dict
company_vendor_sync_body_dict = company_vendor_sync_body_instance.to_dict()
# create an instance of CompanyVendorSyncBody from a dict
company_vendor_sync_body_from_dict = CompanyVendorSyncBody.from_dict(company_vendor_sync_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


