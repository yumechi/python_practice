Feature: advanced given function feature
  Advanced given feature.
  We can use """ block and get `context.text`

  Scenario: context sample scenario
    Given a sample text loaded into the frobulator
        """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
        eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """
    When we activate the frobulator
    Then we will find it similar to English

  Scenario: table sample scenario
    Given a set of specific users
       | name      | department  |
       | Barry     | Beer Cans   |
       | Pudey     | Silly Walks |
       | Two-Lumps | Silly Walks |

     When we count the number of people in each department
     Then we will find two people in "Silly Walks"
      But we will find one person in "Beer Cans"
