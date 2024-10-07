# BusinessNormalViewTags

Tags to indicate the current status of business

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim_status** | **str** | Indicates that a claim request was made for the business and request is in consideration | [optional] 
**approval_status** | **str** | Indicates that an approval request was made for the business and request is in consideration | [optional] 
**publishable** | **str** | Indicates that a business can be published | [optional] 

## Example

```python
from procore_sdk.models.business_normal_view_tags import BusinessNormalViewTags

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessNormalViewTags from a JSON string
business_normal_view_tags_instance = BusinessNormalViewTags.from_json(json)
# print the JSON string representation of the object
print(BusinessNormalViewTags.to_json())

# convert the object into a dict
business_normal_view_tags_dict = business_normal_view_tags_instance.to_dict()
# create an instance of BusinessNormalViewTags from a dict
business_normal_view_tags_from_dict = BusinessNormalViewTags.from_dict(business_normal_view_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


