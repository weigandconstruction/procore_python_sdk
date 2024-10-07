# BusinessNormalViewProvidedServicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Provided Service UUID | [optional] 
**key** | **str** | i18n key for the name of the Provided Service | [optional] 
**path** | **str** | The keys of the Provided Service hierarchy, e.g. key1#key2#key3 | [optional] 
**level** | **str** | The name of this Provided Service&#39;s level, ex. &#39;trade&#39; or &#39;category&#39; | [optional] 

## Example

```python
from procore_sdk.models.business_normal_view_provided_services_inner import BusinessNormalViewProvidedServicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessNormalViewProvidedServicesInner from a JSON string
business_normal_view_provided_services_inner_instance = BusinessNormalViewProvidedServicesInner.from_json(json)
# print the JSON string representation of the object
print(BusinessNormalViewProvidedServicesInner.to_json())

# convert the object into a dict
business_normal_view_provided_services_inner_dict = business_normal_view_provided_services_inner_instance.to_dict()
# create an instance of BusinessNormalViewProvidedServicesInner from a dict
business_normal_view_provided_services_inner_from_dict = BusinessNormalViewProvidedServicesInner.from_dict(business_normal_view_provided_services_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


