# Checklist4AllOfSectionsAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Section | [optional] 
**position** | **int** | The Position of the Section on the Checklist | [optional] 
**items_attributes** | [**List[Checklist4AllOfSectionsAttributesInnerItemsAttributesInner]**](Checklist4AllOfSectionsAttributesInnerItemsAttributesInner.md) | An array of hashes of the Section&#39;s Item attributes | [optional] 

## Example

```python
from procore_sdk.models.checklist4_all_of_sections_attributes_inner import Checklist4AllOfSectionsAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of Checklist4AllOfSectionsAttributesInner from a JSON string
checklist4_all_of_sections_attributes_inner_instance = Checklist4AllOfSectionsAttributesInner.from_json(json)
# print the JSON string representation of the object
print(Checklist4AllOfSectionsAttributesInner.to_json())

# convert the object into a dict
checklist4_all_of_sections_attributes_inner_dict = checklist4_all_of_sections_attributes_inner_instance.to_dict()
# create an instance of Checklist4AllOfSectionsAttributesInner from a dict
checklist4_all_of_sections_attributes_inner_from_dict = Checklist4AllOfSectionsAttributesInner.from_dict(checklist4_all_of_sections_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


