# BusinessNormalViewClassificationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbreviation** | **str** | Abbreviation of the Classification | [optional] 
**key** | **str** | Identifier key of the Classification | [optional] 
**name** | **str** | Name of the Classification | [optional] 

## Example

```python
from procore_sdk.models.business_normal_view_classifications_inner import BusinessNormalViewClassificationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessNormalViewClassificationsInner from a JSON string
business_normal_view_classifications_inner_instance = BusinessNormalViewClassificationsInner.from_json(json)
# print the JSON string representation of the object
print(BusinessNormalViewClassificationsInner.to_json())

# convert the object into a dict
business_normal_view_classifications_inner_dict = business_normal_view_classifications_inner_instance.to_dict()
# create an instance of BusinessNormalViewClassificationsInner from a dict
business_normal_view_classifications_inner_from_dict = BusinessNormalViewClassificationsInner.from_dict(business_normal_view_classifications_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


